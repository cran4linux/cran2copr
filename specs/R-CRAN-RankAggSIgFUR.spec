%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RankAggSIgFUR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Polynomially Bounded Rank Aggregation under Kemeny's Axiomatic Approach

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-plyr 

%description
Polynomially bounded algorithms to aggregate complete rankings under
Kemeny's axiomatic framework. 'RankAggSIgFUR' (pronounced as
rank-agg-cipher) contains two heuristics algorithms: FUR and SIgFUR. For
details, please see Badal and Das (2018) <doi:10.1016/j.cor.2018.06.007>.

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
