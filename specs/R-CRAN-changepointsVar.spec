%global __brp_check_rpaths %{nil}
%global packname  changepointsVar
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Change-Points Detections for Changes in Variance

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-lars 
Requires:         R-MASS 
Requires:         R-CRAN-lars 

%description
Detection of change-points for variance of heteroscedastic Gaussian
variables with piecewise constant variance function. Adelfio, G. (2012),
Change-point detection for variance piecewise constant models,
Communications in Statistics, Simulation and Computation, 41:4, 437-448,
<doi:10.1080/03610918.2011.592248>.

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
