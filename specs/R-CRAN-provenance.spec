%global packname  provenance
%global packver   2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.4
Release:          3%{?dist}
Summary:          Statistical Toolbox for Sedimentary Provenance Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-IsoplotR 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-IsoplotR 

%description
Bundles a number of established statistical methods to facilitate the
visual interpretation of large datasets in sedimentary geology. Includes
functionality for adaptive kernel density estimation, principal component
analysis, correspondence analysis, multidimensional scaling, generalised
procrustes analysis and individual differences scaling using a variety of
dissimilarity measures. Univariate provenance proxies, such as
single-grain ages or (isotopic) compositions are compared with the
Kolmogorov-Smirnov, Kuiper or Sircombe-Hazelton L2 distances. Categorical
provenance proxies such as chemical compositions are compared with the
Aitchison and Bray-Curtis distances, and point-counting data with the
chi-square distance. Also included are tools to plot compositional and
point-counting data on ternary diagrams and point-counting data on radial
plots, to calculate the sample size required for specified levels of
statistical precision, and to assess the effects of hydraulic sorting on
detrital compositions. Includes an intuitive query-based user interface
for users who are not proficient in R.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/densities.csv
%doc %{rlibdir}/%{packname}/DZ.csv
%doc %{rlibdir}/%{packname}/DZerr.csv
%doc %{rlibdir}/%{packname}/endmembers.csv
%doc %{rlibdir}/%{packname}/HM.csv
%doc %{rlibdir}/%{packname}/Major.csv
%doc %{rlibdir}/%{packname}/PT.csv
%doc %{rlibdir}/%{packname}/PTHM.csv
%doc %{rlibdir}/%{packname}/Trace.csv
%{rlibdir}/%{packname}/INDEX
