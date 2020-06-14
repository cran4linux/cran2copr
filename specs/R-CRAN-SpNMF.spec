%global packname  SpNMF
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          2%{?dist}
Summary:          Supervised NMF

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-NMF 
BuildRequires:    R-stats 
Requires:         R-CRAN-NMF 
Requires:         R-stats 

%description
Non-negative Matrix Factorization(NMF) is a powerful tool for identifying
the key features of microbial communities and a dimension-reduction
method. When we are interested in the differences between the structures
of two groups of communities, supervised NMF(Yun Cai, Hong Gu and Tobby
Kenney (2017),<doi:10.1186/s40168-017-0323-1>) provides a better way to do
this, while retaining all the advantages of NMF -- such as
interpretability, and being based on a simple biological intuition.

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
