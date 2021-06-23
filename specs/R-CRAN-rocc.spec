%global __brp_check_rpaths %{nil}
%global packname  rocc
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          ROC Based Classification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-methods 
Requires:         R-CRAN-ROCR 
Requires:         R-methods 

%description
Functions for a classification method based on receiver operating
characteristics (ROC). Briefly, features are selected according to their
ranked AUC value in the training set. The selected features are merged by
the mean value to form a meta-gene. The samples are ranked by their
meta-gene value and the meta-gene threshold that has the highest accuracy
in splitting the training samples is determined. A new sample is
classified by its meta-gene value relative to the threshold. In the first
place, the package is aimed at two class problems in gene expression data,
but might also apply to other problems.

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
