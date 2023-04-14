%global __brp_check_rpaths %{nil}
%global packname  abd
%global packver   0.2-8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.8
Release:          3%{?dist}%{?buildtag}
Summary:          The Analysis of Biological Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-mosaic 
Requires:         R-nlme 
Requires:         R-lattice 
Requires:         R-grid 
Requires:         R-CRAN-mosaic 

%description
The abd package contains data sets and sample code for The Analysis of
Biological Data by Michael Whitlock and Dolph Schluter (2009; Roberts &
Company Publishers).

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
