%global packname  betadiv
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Estimators of Multiple-Site Dissimilarity Indices for theAssessment of Beta Diversity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-J4R >= 1.0.7
Requires:         R-CRAN-J4R >= 1.0.7

%description
Implement the multiple-site dissimilarity indices of Simpson, Sorensen and
nestedness, which can be used to assess the beta diversity of a
population. These indices were adapted from those developed by Baselga
(2010) <doi:10.1111/j.1466-8238.2009.00490.x> in order to have them
population size-independent. All the details behind the calculation and
estimation of these adapted indices can be found in Fortin et al. (2020)
<doi:10.1111/geb.13080>.

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
%doc %{rlibdir}/%{packname}/betadiversityindices.jar
%doc %{rlibdir}/%{packname}/repicea.jar
%{rlibdir}/%{packname}/INDEX
