%global packname  simplexdesign
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Simplex Design for Stochastic Simulations and Agent Based Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-Rfast >= 1.9.5
BuildRequires:    R-CRAN-DiceDesign >= 1.8.1
BuildRequires:    R-CRAN-GGally >= 1.4.0
BuildRequires:    R-CRAN-progress >= 1.2.2
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-Rfast >= 1.9.5
Requires:         R-CRAN-DiceDesign >= 1.8.1
Requires:         R-CRAN-GGally >= 1.4.0
Requires:         R-CRAN-progress >= 1.2.2
Requires:         R-stats 

%description
Design statistical experiments on agent based models, including a
coordinate exchange algorithm for homogeneous agents, and more generally
any simplex.  There is also an optimization algorithm for the case with
multiple classes of homogeneous agents. See our paper "Uncertainty
Quantification for Models of Homogeneous Agents" for more details when it
is published.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
