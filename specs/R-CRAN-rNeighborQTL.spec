%global packname  rNeighborQTL
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Interval Mapping for Quantitative Trait Loci Underlying NeighborEffects

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-gaston 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-parallel 
Requires:         R-CRAN-gaston 
Requires:         R-Matrix 
Requires:         R-CRAN-qtl 
Requires:         R-parallel 

%description
To enable quantitative trait loci mapping of neighbor effects, this
package extends a single-marker regression to interval mapping. The
theoretical background of the method is described in Sato et al. (2020)
<doi:10.1101/2020.05.20.089474>.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/ColKas_geno.csv
%doc %{rlibdir}/%{packname}/ColKas_pheno.csv
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rNeighborQTL.Rmd
%{rlibdir}/%{packname}/INDEX
