%global __brp_check_rpaths %{nil}
%global packname  DriftBurstHypothesis
%global packver   0.4.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Calculates the Test-Statistic for the Drift Burst Hypothesis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.18
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.18
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 

%description
Calculates the T-Statistic for the drift burst hypothesis from the working
paper Christensen, Oomen and Reno (2018) <DOI:10.2139/ssrn.2842535>. The
authors' MATLAB code is available upon request, see:
<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2842535>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
