%global packname  SmartSifter
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Online Unsupervised Outlier Detection Using Finite Mixtures withDiscounting Learning Algorithms

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rootSolve 

%description
Addressing the problem of outlier detection from the viewpoint of
statistical learning theory. This method is proposed by Yamanishi, K.,
Takeuchi, J., Williams, G. et al. (2004)
<DOI:10.1023/B:DAMI.0000023676.72185.7c>. It learns the probabilistic
model (using a finite mixture model) through an on-line unsupervised
process. After each datum is input, a score will be given with a high one
indicating a high possibility of being a statistical outlier.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
