%global __brp_check_rpaths %{nil}
%global packname  tmvnsim
%global packver   1.0-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Truncated Multivariate Normal Simulation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
Importance sampling from the truncated multivariate normal using the GHK
(Geweke-Hajivassiliou-Keane) simulator. Unlike Gibbs sampling which can
get stuck in one truncation sub-region depending on initial values, this
package allows truncation based on disjoint regions that are created by
truncation of absolute values. The GHK algorithm uses simple Cholesky
transformation followed by recursive simulation of univariate truncated
normals hence there are also no convergence issues. Importance sample is
returned along with sampling weights, based on which, one can calculate
integrals over truncated regions for multivariate normals.

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
