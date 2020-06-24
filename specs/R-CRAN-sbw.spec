%global packname  sbw
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Stable Balancing Weights for Causal Inference and Estimationwith Incomplete Outcome Data

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-quadprog 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-spatstat 
Requires:         R-Matrix 
Requires:         R-CRAN-quadprog 
Requires:         R-CRAN-slam 
Requires:         R-MASS 
Requires:         R-CRAN-spatstat 

%description
Implements the Stable Balancing Weights by Zubizarreta (2015)
<DOI:10.1080/01621459.2015.1023805>. These are the weights of minimum
variance that approximately balance the empirical distribution of the
observed covariates. For an overview, see Chattopadhyay, Hase and
Zubizarreta (2020) <DOI:10.1002/(ISSN)1097-0258>. To solve the
optimization problem in 'sbw', the default solver is 'quadprog', which is
readily available through CRAN. To enhance the performance of 'sbw', users
are encouraged to install other solvers such as 'gurobi' and 'Rmosek',
which require special installation.

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

%files
%{rlibdir}/%{packname}
