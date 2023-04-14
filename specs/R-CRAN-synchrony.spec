%global __brp_check_rpaths %{nil}
%global packname  synchrony
%global packver   0.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.8
Release:          3%{?dist}%{?buildtag}
Summary:          Methods for Computing Spatial, Temporal, and SpatiotemporalStatistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Methods for computing spatial, temporal, and spatiotemporal statistics as
described in Gouhier and Guichard (2014) <doi:10.1111/2041-210X.12188>.
These methods include empirical univariate, bivariate and multivariate
variograms; fitting variogram models; phase locking and synchrony
analysis; generating autocorrelated and cross-correlated matrices.

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
