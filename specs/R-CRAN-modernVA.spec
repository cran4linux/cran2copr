%global packname  modernVA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          An Implementation of Two Modern Education-Based Value-AddedModels

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Provides functions that fit two modern education-based value-added models.
One of these models is the quantile value-added model.  This model permits
estimating a school's value-added based on specific quantiles of the
post-test distribution.  Estimating value-added based on quantiles of the
post-test distribution provides a more complete picture of an education
institution's contribution to learning for students of all abilities. See
Page, G.L.; San Martín, E.; Orellana, J.; Gonzalez, J. (2017)
<doi:10.1111/rssa.12195> for more details.  The second model is a
temporally dependent value-added model. This model takes into account the
temporal dependence that may exist in school performance between two
cohorts in one of two ways.  The first is by modeling school random
effects with a non-stationary AR(1) process.  The second is by modeling
school effects based on previous cohort's post-test performance. In
addition to more efficiently estimating value-added, this model permits
making statements about the persistence of a schools effectiveness. The
standard value-added model is also an option.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
