%global packname  LDATS
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          3%{?dist}%{?buildtag}
Summary:          Latent Dirichlet Allocation Coupled with Time Series Analyses

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-topicmodels 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-extraDistr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-CRAN-mvtnorm 
Requires:         R-nnet 
Requires:         R-CRAN-progress 
Requires:         R-stats 
Requires:         R-CRAN-topicmodels 
Requires:         R-CRAN-viridis 

%description
Combines Latent Dirichlet Allocation (LDA) and Bayesian multinomial time
series methods in a two-stage analysis to quantify dynamics in
high-dimensional temporal data. LDA decomposes multivariate data into
lower-dimension latent groupings, whose relative proportions are modeled
using generalized Bayesian time series models that include abrupt
changepoints and smooth dynamics. The methods are described in Blei et al.
(2003) <doi:10.1162/jmlr.2003.3.4-5.993>, Western and Kleykamp (2004)
<doi:10.1093/pan/mph023>, Venables and Ripley (2002,
ISBN-13:978-0387954578), and Christensen et al. (2018)
<doi:10.1002/ecy.2373>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
