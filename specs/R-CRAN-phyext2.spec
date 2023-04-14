%global __brp_check_rpaths %{nil}
%global packname  phyext2
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          An Extension (for Package 'SigTree') of Some of the Classes inPackage 'phylobase'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-phylobase 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-CRAN-phylobase 
Requires:         R-CRAN-ape 
Requires:         R-grid 
Requires:         R-stats 

%description
Based on (but not identical to) the no-longer-maintained package 'phyext',
provides enhancements to 'phylobase' classes, specifically for use by
package 'SigTree'; provides classes and methods which help users
manipulate branch-annotated trees (as in 'SigTree'); also provides support
for a few other extra features.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
