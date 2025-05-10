%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spheredata
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Students' Performance Dataset in Physics Education Research (SPHERE)

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.50
Requires:         R-core >= 3.50
BuildArch:        noarch

%description
A multidimensional dataset of students' performance assessment in high
school physics. The SPHERE dataset was collected from 497 students in four
public high schools specifically measuring their conceptual understanding,
scientific ability, and attitude toward physics [see Santoso et al. (2024)
<doi:10.17632/88d7m2fv7p.1>]. The data collection was conducted using some
research based assessments established by the physics education research
community. They include the Force Concept Inventory, the Force and Motion
Conceptual Evaluation, the Rotational and Rolling Motion Conceptual
Survey, the Fluid Mechanics Concept Inventory, the Mechanical Waves
Conceptual Survey, the Thermal Concept Evaluation, the Survey of
Thermodynamic Processes and First and Second Laws, the Scientific
Abilities Assessment Rubrics, and the Colorado Learning Attitudes about
Science Survey. Students' attributes related to gender, age, socioeconomic
status, domicile, literacy, physics identity, and test results
administered using teachers' developed items are also reported in this
dataset.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
