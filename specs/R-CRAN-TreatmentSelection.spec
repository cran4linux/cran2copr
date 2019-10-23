%global packname  TreatmentSelection
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Evaluate Treatment Selection Biomarkers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-binom 
BuildRequires:    R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-survival 
Requires:         R-CRAN-binom 
Requires:         R-grid 

%description
A suite of descriptive and inferential methods designed to evaluate one or
more biomarkers for their ability to guide patient treatment
recommendations.  Package includes functions to assess the calibration of
risk models; and plot, evaluate, and compare markers. Please see the
reference Janes H, Brown MD, Huang Y, et al. (2014)
<doi:10.1515/ijb-2012-0052> for further details.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/check.R
%doc %{rlibdir}/%{packname}/example
%doc %{rlibdir}/%{packname}/todo.Rmd
%{rlibdir}/%{packname}/INDEX
