%global packname  RPEnsemble
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          Random Projection Ensemble Classification

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.2
Requires:         R-core >= 3.4.2
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-parallel 
BuildRequires:    R-class 
BuildRequires:    R-stats 
Requires:         R-MASS 
Requires:         R-parallel 
Requires:         R-class 
Requires:         R-stats 

%description
Implements the methodology of "Cannings, T. I. and Samworth, R. J. (2017)
Random-projection ensemble classification, J. Roy. Stat. Soc., Ser. B.
(with discussion), 79, 959--1035". The random projection ensemble
classifier is a general method for classification of high-dimensional
data, based on careful combination of the results of applying an arbitrary
base classifier to random projections of the feature vectors into a
lower-dimensional space. The random projections are divided into
non-overlapping blocks, and within each block the projection yielding the
smallest estimate of the test error is selected. The random projection
ensemble classifier then aggregates the results of applying the base
classifier on the selected projections, with a data-driven voting
threshold to determine the final assignment.

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
