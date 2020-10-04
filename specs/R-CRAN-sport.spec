%global packname  sport
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          3%{?dist}%{?buildtag}
Summary:          Sequential Pairwise Online Rating Techniques

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-ggplot2 

%description
Calculates ratings for two-player or multi-player challenges. Methods
included in package such as are able to estimate ratings (players
strengths) and their evolution in time, also able to predict output of
challenge. Algorithms are based on Bayesian Approximation Method, and they
don't involve any matrix inversions nor likelihood estimation. Parameters
are updated sequentially, and computation doesn't require any additional
RAM to make estimation feasible. Additionally, base of the package is
written in C++ what makes sport computation even faster. Methods used in
the package refers to Mark E. Glickman (1999)
<http://www.glicko.net/research/glicko.pdf>; Mark E. Glickman (2001)
<doi:10.1080/02664760120059219>; Ruby C. Weng, Chih-Jen Lin (2011)
<http://jmlr.csail.mit.edu/papers/volume12/weng11a/weng11a.pdf>; W. Penny,
Stephen J. Roberts (1999) <doi:10.1109/IJCNN.1999.832603>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
