%global __brp_check_rpaths %{nil}
%global packname  svyweight
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Quick and Flexible Survey Weighting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.00
Requires:         R-core >= 3.5.00
BuildArch:        noarch
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-stats 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-gdata 
Requires:         R-stats 

%description
Quickly and flexibly calculates weights for survey data, in order to
correct for survey non-response or other sampling issues. Uses rake
weighting, a common technique also know as rim weighting or iterative
proportional fitting.  This technique allows for weighting on multiple
variables, even when the interlocked distribution of the two variables is
not known. Interacts with Thomas Lumley's 'survey' package, as described
in Lumley, Thomas (2011, ISBN:978-1-118-21093-2). Adds additional
functionality, more adaptable syntax, and error-checking to the base
weighting functionality in 'survey.'

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
