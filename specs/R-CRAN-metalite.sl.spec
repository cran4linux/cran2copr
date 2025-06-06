%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  metalite.sl
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Subject-Level Analysis Using 'metalite'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-metalite 
BuildRequires:    R-CRAN-metalite.ae 
BuildRequires:    R-CRAN-r2rtf 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-CRAN-uuid 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-metalite 
Requires:         R-CRAN-metalite.ae 
Requires:         R-CRAN-r2rtf 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-brew 
Requires:         R-CRAN-uuid 

%description
Analyzes subject-level data in clinical trials using the 'metalite' data
structure. The package simplifies the workflow to create production-ready
tables, listings, and figures discussed in the subject-level analysis
chapters of "R for Clinical Study Reports and Submission" by Zhang et al.
(2022) <https://r4csr.org/>.

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
