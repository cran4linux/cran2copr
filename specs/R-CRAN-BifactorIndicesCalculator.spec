%global packname  BifactorIndicesCalculator
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Bifactor Indices Calculator

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-CRAN-MplusAutomation 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-mirt 
Requires:         R-CRAN-MplusAutomation 

%description
The calculator computes bifactor indices such as explained common variance
(ECV), hierarchical Omega (OmegaH), percentage of uncontaminated
correlations (PUC), item explained common variance (I-ECV), and more. This
package is an R version of the 'Excel' based 'Bifactor Indices Calculator'
(Dueber, 2017) <doi:10.13023/edp.tool.01> with added convenience features
for directly utilizing output from several programs that can fit
confirmatory factor analysis or item response models.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
