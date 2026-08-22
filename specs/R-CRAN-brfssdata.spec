%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  brfssdata
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access CDC Behavioral Risk Factor Surveillance System Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-duckdb >= 1.5.5
BuildRequires:    R-CRAN-srvyr >= 1.0.0
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-duckdb >= 1.5.5
Requires:         R-CRAN-srvyr >= 1.0.0
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-tools 
Requires:         R-utils 

%description
Download, cache, and analyze annual microdata from the United States
Centers for Disease Control and Prevention Behavioral Risk Factor
Surveillance System (BRFSS) <https://www.cdc.gov/brfss/>. Each requested
survey year is downloaded once as a compact file hosted on public
releases, verified against a published checksum, and cached locally;
queries then run through 'DuckDB' (via the 'duckdb' package), so column
selection and repeat analyses never re-transfer data. Survey-design
helpers construct 'srvyr' design objects with year-appropriate weights,
strata, and primary sampling units, including explicit handling of the
2011 weighting methodology change and of the codes CDC uses for
missing-type answers.

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
