%global packname  greyzoneSurv
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Fit a Grey-Zone Model with Survival Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats4 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-survAUC 
Requires:         R-stats4 
Requires:         R-survival 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-survAUC 

%description
Allows one to classify patients into low, intermediate, and high risk
groups for disease progression based on a continuous marker that is
associated with progression-free survival. It uses a latent class model to
link the marker and survival outcome and produces two cutoffs for the
marker to divide patients into three groups. See the References section
for more details.

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
%{rlibdir}/%{packname}/INDEX
