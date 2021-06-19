%global packname  sbw
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Stable Balancing Weights for Causal Inference and Missing Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-spatstat.geom 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-spatstat.geom 

%description
Implements the Stable Balancing Weights by Zubizarreta (2015)
<DOI:10.1080/01621459.2015.1023805>. These are the weights of minimum
variance that approximately balance the empirical distribution of the
observed covariates. For an overview, see Chattopadhyay, Hase and
Zubizarreta (2020) <DOI:10.1002/(ISSN)1097-0258>. To solve the
optimization problem in 'sbw', the default solver is 'quadprog', which is
readily available through CRAN. To enhance the performance of 'sbw', users
are encouraged to install other solvers such as 'gurobi' and 'Rmosek',
which require special installation. For the installation of gurobi and
pogs, please follow the instructions at
<https://www.gurobi.com/documentation/9.1/quickstart_mac/r_ins_the_r_package.html>
and <http://foges.github.io/pogs/stp/r>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
