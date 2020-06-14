%global packname  EcoSimR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Null Model Analysis for Ecological Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-MASS 
Requires:         R-MASS 

%description
Given a site by species interaction matrix, users can make inferences
about species interactions by performance hypothesis comparing test
statistics against a null distribution. The current package provides
algorithms and metrics for niche-overlap, body size ratios and species
co-occurrence. Users can also integrate their own algorithms and metrics
within these frameworks or completely novel null models. Detailed
explanations about the underlying assumptions of null model analysis in
ecology can be found at http://ecosimr.org.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/burnin.png
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/cooc_hist.png
%doc %{rlibdir}/%{packname}/cooc.png
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/niche_hist.png
%doc %{rlibdir}/%{packname}/niche.png
%doc %{rlibdir}/%{packname}/size_hist.png
%doc %{rlibdir}/%{packname}/size.png
%{rlibdir}/%{packname}/INDEX
