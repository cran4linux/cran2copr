%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DisImpact
%global packver   0.0.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.21
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates Disproportionate Impact When Binary Success Data are Disaggregated by Subgroups

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.14.2
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-duckdb >= 0.5.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-sets 
Requires:         R-CRAN-data.table >= 1.14.2
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-duckdb >= 0.5.0
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-parallel 
Requires:         R-CRAN-fst 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-sets 

%description
Implements methods for calculating disproportionate impact: the percentage
point gap, proportionality index, and the 80%% index. California Community
Colleges Chancellor's Office (2017).  Percentage Point Gap Method.
<https://www.cccco.edu/-/media/CCCCO-Website/About-Us/Divisions/Digital-Innovation-and-Infrastructure/Research/Files/PercentagePointGapMethod2017.ashx>.
California Community Colleges Chancellor's Office (2014).  Guidelines for
Measuring Disproportionate Impact in Equity Plans.
<https://www.cccco.edu/-/media/CCCCO-Website/Files/DII/guidelines-for-measuring-disproportionate-impact-in-equity-plans-tfa-ada.pdf>.

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
