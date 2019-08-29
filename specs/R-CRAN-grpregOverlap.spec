%global packname  grpregOverlap
%global packver   2.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          Penalized Regression Models with Overlapping Grouped Covariates

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-grpreg >= 3.0.2
BuildRequires:    R-Matrix 
Requires:         R-CRAN-grpreg >= 3.0.2
Requires:         R-Matrix 

%description
Fit the regularization path of linear, logistic or Cox models with
overlapping grouped covariates based on the latent group lasso approach.
Latent group MCP/SCAD as well as bi-level selection methods, namely the
group exponential lasso and the composite MCP are also available. This
package serves as an extension of R package 'grpreg' (by Dr. Patrick
Breheny <patrick-breheny@uiowa.edu>) for grouped variable selection
involving overlaps between groups.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
