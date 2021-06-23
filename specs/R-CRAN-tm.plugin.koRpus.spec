%global __brp_check_rpaths %{nil}
%global packname  tm.plugin.koRpus
%global packver   0.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Full Corpus Support for the 'koRpus' Package

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-koRpus >= 0.13.1
BuildRequires:    R-CRAN-sylly >= 0.1.6
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-NLP 
Requires:         R-CRAN-koRpus >= 0.13.1
Requires:         R-CRAN-sylly >= 0.1.6
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-NLP 

%description
Enhances 'koRpus' text object classes and methods to also support large
corpora. Hierarchical ordering of corpus texts into arbitrary categories
will be preserved. Provided classes and methods also improve the ability
of using the 'koRpus' package together with the 'tm' package. To ask for
help, report bugs, suggest feature improvements, or discuss the global
development of the package, please subscribe to the koRpus-dev mailing
list (<https://korpusml.reaktanz.de>).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
