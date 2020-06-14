%global packname  MRCV
%global packver   0.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.3
Release:          2%{?dist}
Summary:          Methods for Analyzing Multiple Response Categorical Variables(MRCVs)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tables 
Requires:         R-CRAN-tables 

%description
The MRCV package provides functions for analyzing the association between
one single response categorical variable (SRCV) and one multiple response
categorical variable (MRCV), or between two or three MRCVs.  A modified
Pearson chi-square statistic can be used to test for marginal independence
for the one or two MRCV case, or a more general loglinear modeling
approach can be used to examine various other structures of association
for the two or three MRCV case.  Bootstrap- and asymptotic-based
standardized residuals and model-predicted odds ratios are available, in
addition to other descriptive information.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
