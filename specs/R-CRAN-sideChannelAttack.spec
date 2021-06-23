%global __brp_check_rpaths %{nil}
%global packname  sideChannelAttack
%global packver   1.0-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          3%{?dist}%{?buildtag}
Summary:          Side Channel Attack

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-mmap 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-CRAN-infotheo 
Requires:         R-MASS 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-mmap 
Requires:         R-CRAN-ade4 
Requires:         R-CRAN-infotheo 

%description
This package has many purposes: first, it gives to the community an R
implementation of each known side channel attack and countermeasures as
well as data to test it, second it allows to implement a side channel
attack quickly and easily.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
