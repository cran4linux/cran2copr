%global packname  slimrec
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Sparse Linear Method to Predict Ratings and Top-NRecommendations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.3
Requires:         R-core >= 3.3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-bigmemory >= 4.5.19
BuildRequires:    R-stats >= 3.3.3
BuildRequires:    R-parallel >= 3.3.3
BuildRequires:    R-CRAN-glmnet >= 2.0.5
BuildRequires:    R-CRAN-pbapply >= 1.3.2
BuildRequires:    R-Matrix >= 1.2.8
BuildRequires:    R-CRAN-assertthat >= 0.1
Requires:         R-CRAN-bigmemory >= 4.5.19
Requires:         R-stats >= 3.3.3
Requires:         R-parallel >= 3.3.3
Requires:         R-CRAN-glmnet >= 2.0.5
Requires:         R-CRAN-pbapply >= 1.3.2
Requires:         R-Matrix >= 1.2.8
Requires:         R-CRAN-assertthat >= 0.1

%description
Sparse Linear Method(SLIM) predicts ratings and top-n recommendations
suited for sparse implicit positive feedback systems. SLIM is decomposed
into multiple elasticnet optimization problems which are solved in
parallel over multiple cores. The package is based on "SLIM: Sparse Linear
Methods for Top-N Recommender Systems" by Xia Ning and George Karypis
<doi:10.1109/ICDM.2011.134>.

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
%{rlibdir}/%{packname}/INDEX
