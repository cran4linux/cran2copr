%global __brp_check_rpaths %{nil}
%global packname  hwwntest
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          3%{?dist}%{?buildtag}
Summary:          Tests of White Noise using Wavelets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-polynom 
BuildRequires:    R-CRAN-wavethresh 
Requires:         R-parallel 
Requires:         R-CRAN-polynom 
Requires:         R-CRAN-wavethresh 

%description
Provides methods to test whether time series is consistent with white
noise.

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
