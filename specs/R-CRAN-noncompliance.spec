%global __brp_check_rpaths %{nil}
%global packname  noncompliance
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}%{?buildtag}
Summary:          Causal Inference in the Presence of Treatment NoncomplianceUnder the Binary Instrumental Variable Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-data.table >= 1.9.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
Requires:         R-CRAN-data.table >= 1.9.4
Requires:         R-CRAN-Rcpp >= 0.12.1

%description
A finite-population significance test of the 'sharp' causal null
hypothesis that treatment exposure X has no effect on final outcome Y,
within the principal stratum of Compliers. A generalized likelihood ratio
test statistic is used, and the resulting p-value is exact. Currently, it
is assumed that there are only Compliers and Never Takers in the
population.

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
