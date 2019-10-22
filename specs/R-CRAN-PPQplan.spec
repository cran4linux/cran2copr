%global packname  PPQplan
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Process Performance Qualification (PPQ) Plans in Chemistry,Manufacturing and Controls (CMC) Statistical Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tolerance 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
Requires:         R-CRAN-tolerance 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 

%description
Assessment for statistically-based PPQ sampling plan, including
calculating the passing probability, optimizing the baseline and high
performance cutoff points, visualizing the PPQ plan and power dynamically.
The analytical idea is based on the simulation methods from the textbook
"Burdick, R. K., LeBlond, D. J., Pfahler, L. B., Quiroz, J., Sidor, L.,
Vukovinsky, K., & Zhang, L. (2017). Statistical Methods for CMC
Applications. In Statistical Applications for Chemistry, Manufacturing and
Controls (CMC) in the Pharmaceutical Industry (pp. 227-250). Springer,
Cham."

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
