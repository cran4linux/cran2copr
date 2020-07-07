%global packname  SQB
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}
Summary:          Sequential Bagging on Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-rpart 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-pls 
Requires:         R-rpart 
Requires:         R-parallel 
Requires:         R-CRAN-caret 
Requires:         R-nnet 
Requires:         R-CRAN-pls 

%description
Methodology: Remove one observation. Training the rest of data that are
sampled without replacement and given this observation's input, predict
the response back. Replicate this N times and for each response, take a
sample from these replicates with replacement. Average each responses of
sample and again replicate this step N time for each observation.
Approximate these N new responses by using bootstrap method and generate
another N responses y'. Training these y' and predict to have N responses
of each testing observation. The average of N is the final prediction.
Each observation will do the same.

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
