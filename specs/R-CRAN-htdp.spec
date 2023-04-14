%global __brp_check_rpaths %{nil}
%global packname  htdp
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}%{?buildtag}
Summary:          Horizontal Time Dependent Positioning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
Requires:         R-CRAN-Rcpp >= 0.12.5

%description
Provides bindings to the National Geodetic Survey (NGS) Horizontal Time
Dependent Positioning (HTDP) utility, v3.2.5, written by Richard Snay,
Chris Pearson, and Jarir Saleh of NGS. HTDP is a utility that allows users
to transform positional coordinates across time and between spatial
reference frames. See <https://www.ngs.noaa.gov/TOOLS/Htdp/Htdp.shtml> for
more information.

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
