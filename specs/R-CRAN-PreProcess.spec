%global __brp_check_rpaths %{nil}
%global packname  PreProcess
%global packver   3.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.7
Release:          3%{?dist}%{?buildtag}
Summary:          Basic Functions for Pre-Processing Microarrays

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-oompaBase >= 3.0
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-oompaBase >= 3.0
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides classes to pre-process microarray gene expression data as part of
the OOMPA collection of packages described at
<http://oompa.r-forge.r-project.org/>.

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
