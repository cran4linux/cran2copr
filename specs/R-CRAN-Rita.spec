%global __brp_check_rpaths %{nil}
%global packname  Rita
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Transformations, Normality Testing, and Reporting

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lattice 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-CRAN-lattice 

%description
Automated performance of common transformations used to fulfill parametric
assumptions of normality and identification of the best performing method
for the user. Output for various normality tests (Thode, 2002)
corresponding to the best performing method and a descriptive statistical
report of the input data in its original units (5-number summary and
mathematical moments) are also presented. Lastly, the Rankit, an empirical
normal quantile transformation (ENQT) (Soloman & Sawilowsky, 2009), is
provided to accommodate non-standard use cases and facilitate adoption.
<DOI: 10.1201/9780203910894>. <DOI: 10.22237/jmasm/1257034080>.

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
