%global packname  signnet
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}
Summary:          Methods to Analyse Signed Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Rcpp 
Requires:         R-Matrix 

%description
Methods for the analysis of signed networks. This includes several
measures for structural balance as introduced by Cartwright and Harary
(1956) <doi:10.1037/h0046049>, blockmodeling algorithms from Doreian
(2008) <doi:10.1016/j.socnet.2008.03.005>, various centrality indices, and
projections of signed two-mode networks introduced by Schoch (2020)
<doi:10.1080/0022250X.2019.1711376>.

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
