%global packname  brainKCCA
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Region-Level Connectivity Network Construction via KernelCanonical Correlation Analysis

License:          LGPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CCA 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-elasticnet 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-brainR 
BuildRequires:    R-CRAN-misc3d 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-CCA 
Requires:         R-CRAN-kernlab 
Requires:         R-parallel 
Requires:         R-CRAN-elasticnet 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-brainR 
Requires:         R-CRAN-misc3d 
Requires:         R-CRAN-oro.nifti 
Requires:         R-utils 
Requires:         R-CRAN-knitr 

%description
It is designed to calculate connection between (among) brain regions and
plot connection lines. Also, the summary function is included to summarize
group-level connectivity network. Kang, Jian (2016)
<doi:10.1016/j.neuroimage.2016.06.042>.

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
