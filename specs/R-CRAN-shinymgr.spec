%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinymgr
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Framework for Building, Managing, and Stitching 'shiny' Modules into Reproducible Workflows

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-reactable 
BuildRequires:    R-CRAN-renv 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-shinydashboard 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-reactable 
Requires:         R-CRAN-renv 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-shinydashboard 

%description
A unifying framework for managing and deploying 'shiny' applications that
consist of modules, where an "app" is a tab-based workflow that guides a
user step-by-step through an analysis. The 'shinymgr' app builder
"stitches" 'shiny' modules together so that outputs from one module serve
as inputs to the next, creating an analysis pipeline that is easy to
implement and maintain. Users of 'shinymgr' apps can save analyses as an
RDS file that fully reproduces the analytic steps and can be ingested into
an R Markdown report for rapid reporting. In short, developers use the
'shinymgr' framework to write modules and seamlessly combine them into
'shiny' apps, and users of these apps can execute reproducible analyses
that can be incorporated into reports for rapid dissemination.

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
