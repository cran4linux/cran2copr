%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  survivalsurrogate
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evaluate a Longitudinal Surrogate with a Censored Outcome

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-rBeta2009 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rpart 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-rBeta2009 
Requires:         R-CRAN-data.table 
Requires:         R-utils 
Requires:         R-CRAN-rpart 

%description
Provides influence function-based methods to evaluate a longitudinal
surrogate marker in a censored time-to-event outcome setting, with plug-in
and targeted minimum loss-based estimation options. More details will be
available in the future in: Agniel D and Parast L (2025+). "Robust
Evaluation of Longitudinal Surrogate Markers with Censored Data." Journal
of the Royal Statistical Society: Series B, In press. A tutorial for this
package can be found at <https://www.laylaparast.com/survivalsurrogate>.

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
