from http import HTTPStatus

import pytest
import allure
from allure_commons.types import Severity

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseResponseSchema, \
    UpdateCourseRequestSchema, GetCoursesQuerySchema, GetCoursesResponseSchema, \
    CreateCourseResponseSchema, CreateCourseRequestSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture
from fixtures.files import FileFixture
from tools.allure.tags import AllureTags
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, \
    assert_get_courses_response, assert_create_course_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTags.REGRESSION, AllureTags.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
class TestCourses:
    @allure.tag(AllureTags.UPDATE_ENTITY)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.title("Update course")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    def test_update_course(self, courses_client: CoursesClient,
                           function_course: CourseFixture):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(
            function_course.response.course.id, request)
        response_data = UpdateCourseResponseSchema.model_validate_json(
            response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_course_response(request, response_data)

        validate_json_schema(response.json(),
                             response_data.model_json_schema())

    @allure.tag(AllureTags.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get courses")
    @allure.severity(Severity.CRITICAL)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_courses(self,
                         courses_client: CoursesClient,
                         function_user: UserFixture,
                         function_course: CourseFixture):
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query)
        response_data = GetCoursesResponseSchema.model_validate_json(
            response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_course.response])
        validate_json_schema(response.json(),
                             response_data.model_json_schema())

    @allure.tag(AllureTags.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create course")
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_course(self,
                           function_user: UserFixture,
                           function_file: FileFixture,
                           courses_client: CoursesClient
                           ):
        request = CreateCourseRequestSchema(
            preview_file_id=function_file.response.file.id,
            created_by_user_id=function_user.response.user.id)
        response = courses_client.create_course_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(
            response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_course_response(request, response_data)
        validate_json_schema(response.json(),
                             response_data.model_json_schema())
