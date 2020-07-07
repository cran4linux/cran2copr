%global packname  FeaLect
%global packver   1.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.20
Release:          3%{?dist}
Summary:          Scores Features for Feature Selection

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lars 
BuildRequires:    R-CRAN-rms 
Requires:         R-CRAN-lars 
Requires:         R-CRAN-rms 

%description
For each feature, a score is computed that can be useful for feature
selection. Several random subsets are sampled from the input data and for
each random subset, various linear models are fitted using lars method. A
score is assigned to each feature based on the tendency of LASSO in
including that feature in the models.Finally, the average score and the
models are returned as the output. The features with relatively low scores
are recommended to be ignored because they can lead to overfitting of the
model to the training data. Moreover, for each random subset, the best set
of features in terms of global error is returned. They are useful for
applying Bolasso, the alternative feature selection method that recommends
the intersection of features subsets.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
