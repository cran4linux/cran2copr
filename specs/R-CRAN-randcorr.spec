%global __brp_check_rpaths %{nil}
%global packname  randcorr
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Generate a Random p x p Correlation Matrix

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Implements the algorithm by Pourahmadi and Wang (2015)
<doi:10.1016/j.spl.2015.06.015> for generating a random p x p correlation
matrix. Briefly, the idea is to represent the correlation matrix using
Cholesky factorization and p(p-1)/2 hyperspherical coordinates (i.e.,
angles), sample the angles from a particular distribution and then convert
to the standard correlation matrix form. The angles are sampled from a
distribution with pdf proportional to sin^k(theta) (0 < theta < pi, k >=
1) using the efficient sampling algorithm described in Enes Makalic and
Daniel F. Schmidt (2018) <arXiv:1809.05212>.

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
