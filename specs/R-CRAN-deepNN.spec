%global __brp_check_rpaths %{nil}
%global packname  deepNN
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Deep Learning

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-Matrix 
Requires:         R-methods 

%description
Implementation of some Deep Learning methods. Includes multilayer
perceptron, different activation functions, regularisation strategies,
stochastic gradient descent and dropout. Thanks go to the following
references for helping to inspire and develop the package: Ian Goodfellow,
Yoshua Bengio, Aaron Courville, Francis Bach (2016, ISBN:978-0262035613)
Deep Learning. Terrence J. Sejnowski (2018, ISBN:978-0262038034) The Deep
Learning Revolution. Grant Sanderson (3brown1blue)
<https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi>
Neural Networks YouTube playlist. Michael A. Nielsen
<http://neuralnetworksanddeeplearning.com/> Neural Networks and Deep
Learning.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
