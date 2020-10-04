%global packname  DNMF
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Discriminant Non-Negative Matrix Factorization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-Matrix 
Requires:         R-CRAN-gplots 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Discriminant Non-Negative Matrix Factorization aims to extend the
Non-negative Matrix Factorization algorithm in order to extract features
that enforce not only the spatial locality, but also the separability
between classes in a discriminant manner. It refers to three article,
Zafeiriou, Stefanos, et al. "Exploiting discriminant information in
nonnegative matrix factorization with application to frontal face
verification." Neural Networks, IEEE Transactions on 17.3 (2006): 683-695.
Kim, Bo-Kyeong, and Soo-Young Lee. "Spectral Feature Extraction Using dNMF
for Emotion Recognition in Vowel Sounds." Neural Information Processing.
Springer Berlin Heidelberg, 2013. and Lee, Soo-Young, Hyun-Ah Song, and
Shun-ichi Amari. "A new discriminant NMF algorithm and its application to
the extraction of subtle emotional differences in speech." Cognitive
neurodynamics 6.6 (2012): 525-535.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
