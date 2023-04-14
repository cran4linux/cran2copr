%global __brp_check_rpaths %{nil}
%global packname  subgxe
%global packver   0.9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.0
Release:          3%{?dist}%{?buildtag}
Summary:          Combine Multiple GWAS by Using Gene-Environment Interactions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Classical methods for combining summary data from genome-wide association
studies (GWAS) only use marginal genetic effects and power can be
compromised in the presence of heterogeneity. 'subgxe' is a R package that
implements p-value assisted subset testing for association (pASTA), a
method developed by Yu et al. (2019) <doi:10.1159/000496867>. pASTA
generalizes association analysis based on subsets by incorporating
gene-environment interactions into the testing procedure.

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
