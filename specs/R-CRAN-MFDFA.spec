%global __brp_check_rpaths %{nil}
%global packname  MFDFA
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          MultiFractal Detrended Fluctuation Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-numbers 
Requires:         R-CRAN-numbers 

%description
Contains the MultiFractal Detrended Fluctuation Analysis (MFDFA),
MultiFractal Detrended Cross-Correlation Analysis (MFXDFA), and the
Multiscale Multifractal Analysis (MMA). The MFDFA() function proposed in
this package was used in Laib et al. (<doi:10.1016/j.chaos.2018.02.024>
and <doi:10.1063/1.5022737>). See references for more information.
Interested users can find a parallel version of the MFDFA() function on
GitHub.

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
