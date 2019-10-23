%global packname  RandPro
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Random Projection with Classification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-caret 
Requires:         R-stats 
Requires:         R-CRAN-e1071 

%description
Performs random projection using Johnson-Lindenstrauss (JL) Lemma (see
William B.Johnson and Joram Lindenstrauss (1984)
<doi:10.1090/conm/026/737400>). Random Projection is a dimension reduction
technique, where the data in the high dimensional space is projected into
the low dimensional space using JL transform. The original high
dimensional data matrix is multiplied with the low dimensional projection
matrix which results in reduced matrix. The projection matrix can be
generated using the projection function that is independent to the
original data. Then finally apply the classification task on the projected
data.

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
