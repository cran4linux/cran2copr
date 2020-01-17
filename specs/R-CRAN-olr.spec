%global packname  olr
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Optimal Linear Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-plyr 
Requires:         R-utils 
Requires:         R-stats 

%description
The optimal linear regression olr(), runs all the possible combinations of
linear regression equations. The olr() returns the equation which has the
greatest adjusted R-squared term or the greatest R-squared term based on
the user's discretion. Essentially, the olr() returns the best fit
equation out of all the possible equations. R-squared increases with the
addition of an explanatory variable whether it is 'significant' or not,
thus this was developed to eliminate that conundrum. Adjusted R-squared is
preferred to overcome this phenomenon, but each combination will still
produce different results and this will return the best one. Complimentary
functions are included which list all of the equations, all of the
equations in ascending order, a function to give the user a specific
model's summary, and the list of adjusted R-squared terms & R-squared
terms. A 'Python' version is available at:
<https://pypi.org/project/olr/>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
